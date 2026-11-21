
import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
    """
    S     = Current stock price
    K     = Strike price
    T     = Time to expiration (years)
    r     = Risk-free interest rate (decimal)
    sigma = Annual volatility (decimal)
    """

    d1 = (
        math.log(S / K) + (r + sigma**2 / 2) * T
    ) / (sigma * math.sqrt(T))

    d2 = d1 - sigma * math.sqrt(T)

    call_price = (
        S * norm.cdf(d1)
        - K * math.exp(-r * T) * norm.cdf(d2)
    )

    put_price = (
        K * math.exp(-r * T) * norm.cdf(-d2)
        - S * norm.cdf(-d1)
    )

    return call_price, put_price


# Input parameters
S = float(input("Current stock price: "))
K = float(input("Strike price: "))
T = float(input("Time to expiration (years): "))
r = float(input("Risk-free interest rate (%): ")) / 100
sigma = float(input("Annual volatility (%): ")) / 100

# Calculate
call, put = black_scholes(S, K, T, r, sigma)

print("\n--- BLACK-SCHOLES RESULTS ---")
print(f"European Call Option: {call:.2f}")
print(f"European Put Option:  {put:.2f}")
