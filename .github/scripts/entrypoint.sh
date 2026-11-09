
#!/bin/bash

cd /app

echo "Starting Task Manager..."

# Run the task manager and save its output
python3 .github/scripts/todo.py | tee task_output.txt

# Run unit tests and save their output
python3 .github/scripts/todo-test.py 2>&1 | tee test_output.txt

# Update the project index
bash .github/scripts/update_index.sh task_output.txt test_output.txt

echo "Process completed!"
