# Domain Workflow: Finance / Trading

## Archetype
`data-pipeline` / `research-ml`

## Phases
1. **Research** — strategy hypothesis, backtest setup, data sourcing
2. **Backtest** — historical simulation, risk metrics, drawdown analysis
3. **Paper Trade** — live simulation with fake capital
4. **Deploy** — live trading with position limits, kill switches
5. **Monitor** — P&L, Sharpe, MaxDD, regime detection

## Agents
- **Quant Researcher** — alpha research + backtesting
- **Risk Manager** — position sizing + limits + stress tests
- **ML Engineer** — signal generation + execution optimization

## Verification
- Backtest includes transaction costs + slippage
- Out-of-sample validation
- Risk limits enforced at infrastructure level
- Audit trail for every trade

## Timebox
4 weeks (T2)
