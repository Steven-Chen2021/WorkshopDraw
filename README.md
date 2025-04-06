# Random Draw Application

This project is a web application that randomly matches attendees to 10 different quizzes and displays the results on a web page. It also allows exporting the results to a `.txt` file, which is saved in a dedicated `log` folder.

## Project Structure

```
random-draw-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── styles.css
├── log
│   └── random_draw_results.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd random-draw-app
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app/main.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

3. Click the **"Generate Random Draw"** button to randomly assign quizzes to attendees. The results will be displayed in a table format with columns: **Line No.**, **Attendee**, and **Quiz**.

4. To export the results, click the **"Export Results"** button. The results will be saved as a `.txt` file in the `log` folder, and the file will also be available for download.

## Features

- Randomly matches attendees to quizzes.
- Displays the draw results in a table format on the web page.
- Exports the results to a `.txt` file saved in the `log` folder.
- Simple and user-friendly interface.

## Log File Example

The exported log file (`log/random_draw_results.txt`) will look like this:

```
Line No. | Attendee - Quiz Mapping:

1. Terry Tseng: Scenario 1: Email Summary Generator
2. Chester Lee: Scenario 2: CSV Data Cleaner
3. Wilson Huang: Scenario 3: Job Listings Aggregator
...
```

## License

This project is licensed under the MIT License.