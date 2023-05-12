from flask import Flask,render_template,request
import yfinance as yf
import os

app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == "POST":
        tic = str(request.form.get('name'))
        print(tic)
        ticker = yf.Ticker(tic).info
        sumary=ticker["longBusinessSummary"]
        sum=ticker["longName"]
        # print(sumary[0:30])
        MarketPrice=ticker["currentPrice"]
        PreviousClosePrice=ticker['regularMarketPreviousClose']
        Volume=ticker["volume"]
        start_date = '2023-01-09'
        end_date = '2023-05-09'
        data = yf.download(tic, start_date, end_date)
        df=data.tail()
        print(os.getcwd())
        os.chdir("C:\\Users\\hp\\Desktop\\Logis\\static")
        print(os.getcwd())
        df.to_csv('file1.csv')
        name_of_file="file1.csv"
        return render_template("index.html",MarketPrice=MarketPrice,PreviousClosePrice=PreviousClosePrice,Volume=Volume,name_of_file=name_of_file,sumary=sumary[0:600],sum=sum)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)