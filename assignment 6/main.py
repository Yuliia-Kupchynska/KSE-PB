# Отримала потрібні дані через бібліотеку yfinance
import yfinance as yf

# Потрібні дані у форматі Dataframe
df = yf.Ticker("PLTR")
df = df.history(period='1y')
df = df[['Open','High', 'Low', 'Close', 'Volume']]

# Розрахунок ковзних середніх
short_window = 20
long_window = 100

df['Short_MA'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['Long_MA'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# Додаємо волатильність для фільтрації слабких сигналів
df['Volatility'] = df['Close'].rolling(window=20).std()

# Генеруємо сигнали з урахуванням волатильності
df['Signal'] = 0

# Купівля тільки якщо різниця MA більше ніж 10% від волатильності
df.loc[(df['Short_MA'] > df['Long_MA']) &
      ((df['Short_MA'] - df['Long_MA']) > 0.1*df['Volatility']), 'Signal'] = 1

# Продаж тільки якщо різниця MA більше ніж 10% від волатильності
df.loc[(df['Short_MA'] < df['Long_MA']) &
      ((df['Long_MA'] - df['Short_MA']) > 0.1*df['Volatility']), 'Signal'] = -1

# Визначаємо зміни позицій
df['Position'] = df['Signal'].diff()

print(df.tail(20))