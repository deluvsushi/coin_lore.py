from requests import get

class CoinLore:
	def __init__(self):
		self.api = "https://api.coinlore.net/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
		}
	
	def get_global_crypto_data(self):
		return get(
			f"{self.api}/global", headers=self.headers).json()
	
	def get_all_coins(self, start: int, limit: int):
		return get(
			f"{self.api}/tickers?start={start}&limit={limit}",
			headers=self.headers).json()
	
	def get_specific_coin(self, coin_id: int):
		return get(
			f"{self.api}/ticker?id={coin_id}",
			headers=self.headers).json()
	
	def get_markets_for_coin(self, coin_id: int):
		return get(
			f"{self.api}/coin/markets?id={coin_id}",
			headers=self.headers).json()
	
	def get_all_exchanges(self):
		return get(
			f"{self.api}/exchanges",
			headers=self.headers).json()
	
	def get_exchange_data(self, exchange_id: int):
		return get(
			f"{self.api}/exchange?id={exchange_id}",
			headers=self.headers).json()
	
	def get_coin_social_stats(self, coin_id: int):
		return get(
			f"{self.api}/social_stats?id={coin_id}",
			headers=self.headers).json()
