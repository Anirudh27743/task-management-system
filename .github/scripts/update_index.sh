
#!/bin/bash

TASK_OUTPUT="$1"
TEST_OUTPUT="$2"

if [ -z "$TASK_OUTPUT" ] || [ -z "$TEST_OUTPUT" ]; then
    echo "Usage: update_index.sh <task_output> <test_output>"
    exit 1
fi

if [ ! -f "$TASK_OUTPUT" ] || [ ! -f "$TEST_OUTPUT" ]; then
    echo "Error: Input files not found."
    exit 1
fi

TODO_TASKS=$(sed -n '/ToDo Tasks:/,/Done Tasks:/p' "$TASK_OUTPUT" | sed '$d')
DONE_TASKS=$(sed -n '/Done Tasks:/,$p' "$TASK_OUTPUT")
TEST_RESULTS=$(cat "$TEST_OUTPUT")

update_section() {
    SECTION="$1"
    CONTENT="$2"

    CONTENT=$(printf '%s' "$CONTENT" | sed 's/[&/\]/\\&/g')

    perl -0pi -e "s|(<pre id=\"$SECTION\">).*?(</pre>)|\${1}$CONTENT\${2}|s" index.html
}

update_section "todo" "$TODO_TASKS"
update_section "done" "$DONE_TASKS"
update_section "tests" "$TEST_RESULTS"

echo "index.html updated successfully."
