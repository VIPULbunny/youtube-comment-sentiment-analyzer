# 📊 YouTube Comment Sentiment Analyzer

A web application built with **Python, NLP, and Streamlit** that analyzes the sentiment of YouTube video comments (Positive, Negative, Neutral) using the **VADER Sentiment Analysis** model.

![ppt architecture](https://github.com/user-attachments/assets/ee249d27-6f30-4939-8e0e-f735ad47eb41)


---

## 🚀 Features

* ✅ Fetches comments directly from YouTube using **YouTube Data API**
* ✅ Analyzes sentiment using **VADER (Valence Aware Dictionary and sEntiment Reasoner)**
* ✅ Displays results with **Pie Chart visualization**
* ✅ Shows **individual comments** with sentiment labels
* ✅ Simple **Streamlit Web UI** for easy use

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries & Frameworks:**

  * `streamlit` – for web app
  * `google-api-python-client` – YouTube API
  * `vaderSentiment` – sentiment analysis
  * `matplotlib` – data visualization
  * `pandas`, `numpy` – data handling

---

## 📂 Project Structure

```
📦 youtube-sentiment-analyzer
 ┣ 📜 project1.py          # Main Streamlit app
 ┣ 📜 requirements.txt     # Dependencies
 ┣ 📜 README.md            # Project Documentation
 ┣ 📂 assets/              # (Optional: store images/diagrams)
```

---

## ⚙️ Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/youtube-sentiment-analyzer.git
cd youtube-sentiment-analyzer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Get a **YouTube Data API Key** from [Google Cloud Console](https://console.cloud.google.com/).

4. Add your API key inside the code (`project1.py`):

```python
api_key = "YOUR_YOUTUBE_API_KEY"
```

5. Run the Streamlit app:

```bash
streamlit run project1.py
```

---

## 📊 Usage

1. Enter a **YouTube Video URL** in the web app.
2. Click **Analyze**.
3. View:

   * Individual comments with sentiment labels
   * Pie chart visualization of sentiment distribution

---

## 📷 Screenshots

 Step 1: Main Page for Input 
 
 <img width="649" height="319" alt="image" src="https://github.com/user-attachments/assets/a8e4a057-978d-4a25-bafb-0dc0c56b9db1" />
 
 - Copy link/URL form Youtube

 <img width="653" height="206" alt="image" src="https://github.com/user-attachments/assets/dd1195cc-c295-4b94-8304-821a22d1a438" />
 
- Streamlit web page

Step 2: Input Submission The user pastes a YouTube video URL (e.g., https://www.youtube.com/watch?v=0_FH6sSDiXI) into the input field and clicks the "Submit" button.

<img width="644" height="235" alt="image" src="https://github.com/user-attachments/assets/d1735bec-f7b1-49e5-ae94-23312ed3837f" />

- Input page (Description: The same page as Fig. 3.1, but now the text input box is filled with a sample YouTube URL.)

Step 3: Processing and Output Display After the user clicks submit, the application processes the request in the background. The page updates to display the results, which include a pie chart showing the distribution of sentiments and a list of sample comments with their classifications.
 
<img width="644" height="293" alt="image" src="https://github.com/user-attachments/assets/d9c46ce2-7882-44f2-a317-788c96467625" />
<img width="643" height="290" alt="image" src="https://github.com/user-attachments/assets/3f203423-f73f-4c4f-b117-68c8c582332f" />
<img width="644" height="285" alt="image" src="https://github.com/user-attachments/assets/35917d70-f7a0-4b80-bac1-797f94115feb" />

- Text processing and summarized output (Description: The page now has two main sections. On the left, a Matplotlib pie chart titled "Sentiment Distribution" shows the percentages of Positive (green), Negative (red), and Neutral (blue) comments. On the right, a list of comments is displayed, each with a colored box (green for 🙂, red for 🙁, blue for 😐) indicating its sentiment, followed by the comment text.)
 


---

## 🌍 Applications

* YouTubers: Understand audience reactions
* Brands: Analyze campaign feedback
* Researchers: Public opinion mining
* Education: NLP project for learning

---

## 🔮 Future Enhancements

* Add **BERT/RoBERTa models** for deeper NLP
* Support for **multiple languages**
* Export results as **CSV/Excel**
* Dashboard with **time-based sentiment trends**

---

## 🙌 Author

**Vipul Solanki**
📌 [LinkedIn](https://www.linkedin.com/in/vipulsolanki777/) | [GitHub](https://github.com/VIPULbunny)

