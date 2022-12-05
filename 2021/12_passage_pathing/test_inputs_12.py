# Puzzle input:
start-A
start-b
A-b
b-c
A-c
c-end

     start
     /   \
    A --- b
     \   /
       c
       |
      end

# Example with nodes to start, 1 to end
# Expect: 4
# Got: 1

############################################################

# Puzzle input:
start-A
start-b
A-end
b-end

      start
      /   \
     A     b
      \   /
       end


Expect: 2
Got: 2

############################################################

# Puzzle input:
start-A
A-c
A-end

      start
        |
    c - A
        |
       end


Expect: 2
Got: 2

############################################################

# Puzzle input:
start-A
A-c
A-end
A-d

      start
        |
    c - A - d
        |
       end


Expect: 4
Got: 4