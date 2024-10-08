# For this exercise, then, we’ll assume that you run 10 km each day as part of your exercise regime. You want to know how long, on average, that run takes.

# Write a function (run_timing) that asks how long it took for you to run 10 km. The function continues to ask how long (in minutes) it took for additional runs, until the user presses Enter. At that point, the function exits--but only after calculating and displaying the average time that the 10 km runs took.

def run_timing() -> str:
    run_times = []
    new_time = 0

    while True:
        new_time = input("Enter a 10 km run time: ").strip()
        if not new_time:
            break
        else:
            run_times.append(float(new_time))

    if len(run_times):
        print(f"Average of {sum(run_times) /
              len(run_times):.2f}, over {len(run_times)} runs")
    else:
        print("You didn't provide any times.")


run_timing()
