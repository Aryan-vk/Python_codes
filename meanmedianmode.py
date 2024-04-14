import statistics

def calculate_statistics(data):
    mean = statistics.mean(data)
    mode = statistics.mode(data)
    median = statistics.median(data)
    return mean, mode, median

f = open('data.txt.txt','r')
g = open('opdata.txt.txt','w')
def main( f , g):
    try:
        with open('data.txt.txt', 'r') as input_file:
            # Read data from the file and convert it to a list of numbers
            data = [float(line.strip()) for line in input_file]

        # Calculate statistics
        mean, mode, median = calculate_statistics(data)

        # Write results to the output file
        with open('opdata.txt.txt' , 'w') as output_file:
            output_file.write(f"Mean: {mean}\n")
            output_file.write(f"Mode: {mode}\n")
            output_file.write(f"Median: {median}\n")

        print("Results written to", 'opdata.txt.txt')

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))

#Main function calling
main(f , g)

