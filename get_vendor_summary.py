import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db
logging.basicConfig(
      filename="logs/get_vendor_summary.log",
      level=logging.DEBUG,
      format ="%(asctime)s-%(levelname)s-%(message)s",
      filemode ="a"
  )
def create_vendor_summary(conn):
    '''' this function will merge the different tables to get the overall vendor summary and addingnew columns in the resultant data'''
    vendor_sales_summary = pd.read_sql_query(""" with FreightSummary as (
     SELECT
      VendorNumber,
      SUM(Freight) as FreightCost
     FROM vendor_invoice
     Group by VendorNumber
     ),

     PurchaseSummary as (
     SELECT
     p.VendorNumber,
     p.VendorName,
     p.Brand,
     p.Description,
     p.PurchasePrice,
     pp.Price as ActulPrice,
     pp.Volume,
     Sum(p.Quantity) as TotalPurchaseQuantity,
     Sum(p.Dollars) as TotalPurchaseDollars
     From purchases p
     join purchase_prices pp
       on p.Brand=pp.Brand
      where p.PurchasePrice>0
     group by 
      p.VendorNumber,p.VendorName,p.Brand,p.Description,p.PurchasePrice,pp.Price,pp.Volume
     ),
     SalesSummary As (
     SELECT
       VendorNo,
       Brand,
       Sum(SalesQuantity) as TotalSalesQuantity,
       Sum(SalesDollars) as TotalSalesDollars,
       Sum(SalesPrice) as TotalSalesPrice,
       Sum(ExciseTax) as TotalExciseTax
      From sales
      Group by VendorNo,Brand
     )
     Select
      ps.VendorNumber,
      ps.VendorName,
      ps.Brand,
      ps.Description,
       ps.PurchasePrice,
      ps. ActulPrice,
      ps.Volume,
      ps. TotalPurchaseQuantity,
      ps.TotalPurchaseDollars,
      ss.TotalSalesQuantity,
      ss.TotalSalesDollars,
      ss.TotalSalesPrice,
      ss.TotalExciseTax,
      fs.FreightCost
      From PurchaseSummary as ps
       Left join SalesSummary as ss 
      on ps.VendorNumber=ss.VendorNo
      and ps.Brand==ss.Brand
      Left join freightSummary fs
      on ps.VendorNumber=fs.VendorNumber
      order by ps.TotalPurchaseDollars DESC""",conn)
    return vendor_sales_summary

def clean_data(df):
    ''''this function will clean the data'''
    #changing datatypes to float
    df['Volume']=df['Volume'].astype('float64')

    #filling missing values with 0
    df.fillna(0,inplace=True)

    #removing spaces from categorical columns
     df['VendorName'] = df['VendorName'].str.strip()
     df['Description'] = df['Description'].str.strip()
     # creating new cloumns for better analysis
      vendor_sales-summary['GrossProfit'] = Vendor_sales_summary['TotalSalesDollars']-vendor_sales_summary['TotalPurchaseDollars']
      vendor_sales-summary['ProfitMargin'] = Vendor_sales_summary['GrossProfit']/vendor_sales_summary['TotalSalesDollars'])*100
      vendor_sales_summary['StockTurnover']=vendor_sales_summary['TotalSalesQuantity']/vendor_sales_summary['TotalPurchaseQuantity'] 
      vendor_sales_summary['SalestoPurchaseRatio'] =vendor_sales_summary['TotalSalesDollars']/vendor_sales_summary['TotalPurchaseDollars']
     return df

if__name__=='__main__':
    #creating database connection 
    conn=sqlite3.connect('inventory.db')
    logging.info('Creating Vendor Summary Table.....')
    summary_df=create_vendor_summary(conn)
    logging.info(summary_df.head))
    logging.info('Cleaning Data.....')
    clean_df=clean_data(summary_df)
    logging.info(clean_df.head())
    logging.info('Ingestion Data.....')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')
    