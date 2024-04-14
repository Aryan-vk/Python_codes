import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

def generate_gaussian_curve(peak_height, left_width, right_width, data_size):
    x = np.linspace(-5, 5, data_size)
    gaussian_curve = peak_height * np.exp(-(x**2) / (2 * left_width**2)) + \
                      peak_height * np.exp(-(x**2) / (2 * right_width**2))
    return x, gaussian_curve

def add_random_numbers(data, random_range):
    return data + np.random.uniform(-random_range, random_range, len(data))

def main():
    try:
        # User inputs
        peak_height = float(input("Enter the peak height: "))
        left_width = float(input("Enter the width of the left side of the peak: "))
        right_width = float(input("Enter the width of the right side of the peak: "))
        data_size = int(input("Enter the size of the data (greater than 100): "))
        random_range = float(input("Enter the range for adding random numbers: "))

        if data_size <= 100:
            raise ValueError("Data size must be greater than 100.")

        # Generate Gaussian curve
        x, gaussian_curve = generate_gaussian_curve(peak_height, left_width, right_width, data_size)

        # Add random numbers
        data_with_random = add_random_numbers(gaussian_curve, random_range)

        # Plot the Gaussian curve and data with random numbers
        plt.plot(x, gaussian_curve, label="Original Gaussian Curve", color='blue')
        plt.plot(x, data_with_random, label="Gaussian Curve with Random Numbers", linestyle='dashed', color='red')
        plt.legend()
        plt.title("Gaussian Curve with Random Numbers")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()

        # Calculate skewness and kurtosis
        skewness = skew(data_with_random)
        kurt = kurtosis(data_with_random)

        print(f"Skewness: {skewness}")
        print(f"Kurtosis: {kurt}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

main()
