import twint
import nest_asyncio

nest_asyncio.apply()

c = twint.Config()
c.Search = "healthcare"
c.Limit = 2
c.Custom["tweet"]=["id","created_at","username","tweet"]
c.Since = '2018-12-31'
c.Until = '2019-12-31'
c.Pandas_clean = True
c.Pandas = True

twint.run.Search(c)

Healthtweets_df = twint.storage.panda.Tweets_df
