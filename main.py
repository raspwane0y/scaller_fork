import requests
from bs4 import BeautifulSoup

# URL сайта, который будем парсить
url = 'https://example.com '

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Извлекаем и выводим заголовки h1, h2
    h1 = soup.find('h1')
    print("H1:", h1.text if h1 else "Не найден")

    h2_list = soup.find_all('h2')
    print("\nH2 заголовки:")
    for h2 in h2_list:
        print('-', h2.text)
else:
    print(f"Ошибка загрузки страницы: {response.status_code}")


using System;
using System.Windows.Forms;

namespace CalculatorApp
{
    public partial class Form1 : Form
    {
        private string operation = ""; // Текущая операция
        private double firstNumber = 0; // Первое число
        private bool isOperationPerformed = false; // Флаг для проверки выполнения операции

        public Form1()
        {
            InitializeComponent();
        }

        // Обработка нажатия кнопок с цифрами
        private void NumberButton_Click(object sender, EventArgs e)
        {
            Button button = (Button)sender;

            if (txtDisplay.Text == "0" || isOperationPerformed)
            {
                txtDisplay.Clear();
                isOperationPerformed = false;
            }

            txtDisplay.Text += button.Text;
        }

        // Обработка нажатия кнопок операций
        private void OperationButton_Click(object sender, EventArgs e)
        {
            Button button = (Button)sender;

            if (double.TryParse(txtDisplay.Text, out firstNumber))
            {
                operation = button.Text;
                isOperationPerformed = true;
            }
        }

        // Обработка нажатия кнопки "="
        private void btnEquals_Click(object sender, EventArgs e)
        {
            double secondNumber = 0;
            double result = 0;

            if (double.TryParse(txtDisplay.Text, out secondNumber))
            {
                switch (operation)
                {
                    case "+":
                        result = firstNumber + secondNumber;
                        break;
                    case "-":
                        result = firstNumber - secondNumber;
                        break;
                    case "*":
                        result = firstNumber * secondNumber;
                        break;
                    case "/":
                        if (secondNumber != 0)
                            result = firstNumber / secondNumber;
                        else
                        {
                            MessageBox.Show("Деление на ноль невозможно!");
                            return;
                        }
                        break;
                }

                txtDisplay.Text = result.ToString();
                firstNumber = result;
            }
        }

        // Обработка нажатия кнопки "C"
        private void btnClear_Click(object sender, EventArgs e)
        {
            txtDisplay.Text = "0";
            firstNumber = 0;
            operation = "";
            isOperationPerformed = false;
        }
    }
}
