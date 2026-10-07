"""pump.fun bonding-curve math (constant product on virtual reserves). Fees are charged on the SOL side.
Validated against live Jupiter quotes by research/check_formula.py before it is trusted for backtests."""


def buy_tokens(vsol, vtok, sol_in, fee_frac):
    """SOL in (fee included, exact-in) -> tokens out. Fee taken off the top: the curve sees sol_in / (1 + fee)."""
    net = sol_in / (1 + fee_frac)
    return vtok - (vsol * vtok) / (vsol + net)


def sell_sol(vsol, vtok, tok_in, fee_frac):
    """tokens in -> SOL out after fee."""
    gross = vsol - (vsol * vtok) / (vtok + tok_in)
    return gross * (1 - fee_frac)
