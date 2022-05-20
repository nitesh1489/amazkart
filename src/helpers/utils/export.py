import pandas as pd
import datetime,os
def export_csv(final_data):
        post_data=pd.DataFrame(final_data)
        post_data.to_csv(f"{os.environ.get('OUTPUT_PATH')}/flipkart_{datetime.datetime.now().strftime('%d%m%Y_%H%M')}.csv",encoding="utf-8",sep="|",index=False)