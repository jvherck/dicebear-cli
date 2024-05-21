# See all commands and options
dicebear --help
dicebear -h

# Help menu for the `create` command
dicebear create --help

# Creating an avatar
dicebear create initials --seed "John Apple" --format svg
dicebear create initials -s "John Apple" -f svg

# Creating multiple avatars
dicebear create --format png --count 5
dicebear create -f png -c 5
