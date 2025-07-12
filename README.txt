📄 הוראות התקנה – גרסת Flask לבוט מסחר ב-BingX

1. התקן את הספריות הדרושות:
   pip install -r requirements.txt

2. הפעל את הבוט:
   python main.py

3. השרת יאזין לכתובת:
   http://localhost:10000/webhook

4. ב-TradingView השתמש בכתובת webhook (Render):
   https://your-render-app-name.onrender.com/webhook

5. התוכן של ההתראה יכול להיות:
   {"message": "long"}  או  {"message": "short"}

הבוט ישלח עדכונים לטלגרם שלך ויבצע פעולת מסחר בהתאם.

בהצלחה! 🚀
