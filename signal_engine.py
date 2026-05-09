from structure_engine import get_structure
from liquidity_engine import get_liquidity
from session_filter import is_active_session
from mtf_filter import get_htf_bias
from volatility_filter import get_atr_filter


def generate_signal():

    structure = get_structure()
    liq = get_liquidity()

    htf_bias = get_htf_bias()
    volatility = get_atr_filter()

    score = 0

    # =========================
    # 1. STRUCTURE COMPONENT
    # =========================

    if structure["trend"] == "bullish":
        score += 1
    else:
        score -= 1

    if structure["bos_up"] or structure["choch_up"]:
        score += 2

    if structure["bos_down"] or structure["choch_down"]:
        score -= 2


    # =========================
    # 2. LIQUIDITY COMPONENT
    # =========================

    if liq["sweep_high"]:
        score -= 3

    if liq["sweep_low"]:
        score += 3

    if liq["eq_high"]:
        score -= 1

    if liq["eq_low"]:
        score += 1


    # =========================
    # 3. SAFETY FILTER
    # =========================

    if (structure["bos_up"] and liq["sweep_high"]) or (structure["bos_down"] and liq["sweep_low"]):
        score = 0


    # =========================
    # 4. SESSION FILTER
    # =========================

    if not is_active_session():
        score = 0


    # =========================
    # 5. HTF FILTER (4H BIAS)
    # =========================

    if htf_bias == "bullish" and score < 0:
        score = 0

    if htf_bias == "bearish" and score > 0:
        score = 0


    # =========================
    # 6. VOLATILITY FILTER (ATR)
    # =========================

    if volatility == "low":
        score = 0

    if volatility == "high" and abs(score) < 3:
        score = 0


    # =========================
    # 7. DECISION ENGINE
    # =========================

    if score >= 3:
        action = "LONG"
    elif score <= -3:
        action = "SHORT"
    else:
        action = "NO TRADE"


    price = structure["price"]
    swing_high = structure["swing_high"]
    swing_low = structure["swing_low"]


    # =========================
    # 8. SMART MONEY EXIT ENGINE
    # =========================

    if action == "LONG":
        entry = price
        stop_loss = swing_low
        take_profit_1 = swing_high
        take_profit_2 = swing_high * 1.01

    elif action == "SHORT":
        entry = price
        stop_loss = swing_high
        take_profit_1 = swing_low
        take_profit_2 = swing_low * 0.99

    else:
        entry = None
        stop_loss = None
        take_profit_1 = None
        take_profit_2 = None


    # =========================
    # FINAL OUTPUT
    # =========================

    return {
        "action": action,
        "score": score,
        "price": price,
        "htf_bias": htf_bias,
        "volatility": volatility,
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit_1": take_profit_1,
        "take_profit_2": take_profit_2
    }