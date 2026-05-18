# 📊 Data Visualization & AI Analysis Tool

A modern desktop application for data visualization, multi-file analysis, and AI-powered insights. Think of it as a mini **Power BI + AI Analyst** combining professional data visualization with intelligent data discovery.

## ✨ Key Features

### 📈 Data Visualization
- **Multiple Chart Types**: Bar, Line, Pie, Scatter Plot, Histogram, Box Plot
- **Interactive Charts**: Zoom, pan, and export visualizations
- **Live Updates**: Real-time chart updates as data changes
- **Chart Comparison**: View multiple charts side-by-side

### 📁 Multi-File Analysis
- **Compare Up to 3 Files**: Load and compare CSV files simultaneously
- **Data Merging**: Automatically merge and align datasets
- **Trend Analysis**: Detect growth, drops, and patterns across files
- **Comparative Metrics**: Side-by-side statistical comparisons

### 🤖 AI Insights (Premium Feature)
- **Automated Analysis**: Rule-based insights without API dependency
- **Smart Summaries**: AI-generated insights about your data
- **Trend Prediction**: Predict next data points
- **Anomaly Detection**: Identify unusual patterns
- **Premium AI**: Optional cloud-based LLM integration (OpenAI)

### 🎨 Professional UI
- **Dark Mode Dashboard**: Clean, modern interface
- **Sidebar Navigation**: Easy access to all features
- **Card-Style Analytics**: Organized information presentation
- **Responsive Design**: Adapts to different screen sizes

## 🏗️ Project Structure

```
Data-Viz-Ai-Tool/
├── src/
│   ├── main.py                 # Application entry point
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py      # CustomTkinter main window
│   │   ├── sidebar.py          # Sidebar navigation component
│   │   └── dashboard.py        # Main dashboard area
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py           # CSV file loading
│   │   └── processor.py        # Pandas data processing
│   ├── charts/
│   │   ├── __init__.py
│   │   ├── chart_factory.py    # Chart creation logic
│   │   └── embedder.py         # Matplotlib → CustomTkinter integration
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── analyzer.py         # Data analysis engine
│   │   └── comparator.py       # Multi-file comparison
│   └── ai/
│       ├── __init__.py
│       ├── insights.py         # Free AI insights (scikit-learn)
│       └── premium_ai.py       # Premium AI (LLM integration)
├── requirements.txt            # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

## 📦 Tech Stack

| Component | Tool | Version |
|-----------|------|----------|
| **UI Framework** | CustomTkinter | 5.2.0+ |
| **Data Processing** | Pandas | 2.0.0+ |
| **Visualization** | Matplotlib | 3.7.0+ |
| **Data Analysis** | Scikit-learn | 1.2.0+ |
| **Numerical Computing** | NumPy | 1.24.0+ |
| **Excel Export** | OpenPyXL | 3.10.0+ |
| **API Integration** | Requests | 2.31.0+ |

## 🚀 Build Roadmap

### Phase 1: MVP (Foundation)
- [ ] Single CSV file upload
- [ ] Basic data table view
- [ ] Simple chart display (Bar, Line)
- [ ] Dark mode UI with CustomTkinter

### Phase 2: Core Features
- [ ] Multiple chart types (Pie, Scatter, Histogram, Box)
- [ ] Multi-file comparison (2-3 files)
- [ ] Data filtering and sorting
- [ ] Basic statistics dashboard

### Phase 3: Advanced Features
- [ ] Complete UI redesign with sidebar
- [ ] Export to PDF/Excel
- [ ] Advanced filtering
- [ ] Data refresh capabilities

### Phase 4: Premium Features
- [ ] Free AI insights (rule-based)
- [ ] Premium API integration (OpenAI)
- [ ] Automated predictions
- [ ] Smart data summaries

## 💻 Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/BraveGuru09/Data-Viz-Ai-Tool.git
cd Data-Viz-Ai-Tool
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python src/main.py
```

## 📊 Usage Examples

### Load and Visualize Single File
```python
from src.data.loader import DataLoader
from src.charts.chart_factory import ChartFactory

loader = DataLoader()
df = loader.load_csv("sales_data.csv")

chart_factory = ChartFactory(df)
chart_factory.create_bar_chart("Month", "Sales")
```

### Compare Multiple Files
```python
from src.analytics.comparator import FileComparator

comparator = FileComparator()
comparison = comparator.compare_files([
    "sales_jan.csv",
    "sales_feb.csv",
    "sales_mar.csv"
])

insights = comparison.get_insights()
print(insights)
```

### Get AI Insights
```python
from src.ai.insights import InsightGenerator

generator = InsightGenerator()
insights = generator.analyze(df)
print(insights.get_summary())
print(insights.get_trends())
```

## 🤖 AI Insights Types

### Free Insights (Rule-Based)
- Average/Median calculations
- Trend detection (up/down)
- Outlier identification
- Growth rate calculations

### Premium Insights (AI-Powered)
- Natural language summaries
- Predictive analytics
- Complex pattern recognition
- Recommendation engine

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ by BraveGuru09**