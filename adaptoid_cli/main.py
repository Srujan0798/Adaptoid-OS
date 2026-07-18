"""Bootstrap CLI for Adaptoid OS.

The kit (kernel laws, Ship OS, validators, templates) lives in the git repo —
this package only locates it and delegates, so the repo stays the single truth.

Resolution order for the kit home:
  1. $ADAPTOID_HOME
  2. a checkout containing adaptor/engine.py at or above the current directory
  3. ~/adaptoid-os (cloned on first run)

Everything except the subcommands below is passed straight to adaptor/engine.py:
  adaptoid home        print resolved kit path
  adaptoid update      git pull the kit
  adaptoid conductor … delegate to conductor/conductor.py
"""
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

REPO_URL = "https://github.com/Srujan0798/Adaptoid-OS.git"
DEFAULT_HOME = Path.home() / "adaptoid-os"


def find_checkout() -> Optional[Path]:
    d = Path.cwd()
    for p in (d, *d.parents):
        if (p / "adaptor" / "engine.py").exists():
            return p
    return None


def resolve_home() -> Path:
    env = os.environ.get("ADAPTOID_HOME")
    if env:
        return Path(env).expanduser()
    checkout = find_checkout()
    if checkout is not None:
        return checkout
    return DEFAULT_HOME


def ensure_kit(home: Path) -> None:
    if (home / "adaptor" / "engine.py").exists():
        return
    if home.exists() and any(home.iterdir()):
        sys.exit(
            f"error: {home} exists but is not an Adaptoid OS kit "
            "(no adaptor/engine.py). Set ADAPTOID_HOME to a valid checkout."
        )
    print(f"[adaptoid] kit not found — cloning {REPO_URL} → {home}")
    rc = subprocess.call(["git", "clone", "--depth", "1", REPO_URL, str(home)])
    if rc != 0:
        sys.exit("error: git clone failed (is git installed and the network up?)")


def main() -> None:
    argv = sys.argv[1:]
    home = resolve_home()

    if argv[:1] == ["home"]:
        print(home)
        return

    ensure_kit(home)

    if argv[:1] == ["update"]:
        sys.exit(subprocess.call(["git", "-C", str(home), "pull", "--ff-only"]))

    if argv[:1] == ["conductor"]:
        target = home / "conductor" / "conductor.py"
        sys.exit(subprocess.call([sys.executable, str(target), *argv[1:]]))

    engine = home / "adaptor" / "engine.py"
    sys.exit(subprocess.call([sys.executable, str(engine), *argv]))


if __name__ == "__main__":
    main()
