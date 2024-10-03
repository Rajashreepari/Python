def filter_boxes(stack):
    primary_colors = ['Red', 'Green', 'Blue']
    queue = []
    new_stack = []

    for box in stack:
        if box in primary_colors:
            new_stack.append(box)
        else:
            queue.append(box)

    return new_stack, queue

sstack = ['Purple', 'White', 'Green', 'Orange', 'Red', 'Yellow', 'Magenta', 'Red']

new_stack, queue = filter_boxes(stack)

print("Boxes in the stack after modification:")
for box in new_stack:
    print(box)

print("\nBoxes in the queue:")
for box in queue:
    print(box)
