# custom modules
import custom as c

if __name__ == "__main__":
    print(c.uptext("bob"))

# if you run this file directly, it will call the main() function
# but if you import it from another file, it won't
# so we use a conditional to check what is running this code
# and only execute the main() function when we are running this file
# not when we are importing it.

# this is useful because 90% of the time we will be importing our modules
# but sometimes we want to run them directly, like when testing or debugging
# so we can do that by calling the main() function from within the module
# and then running the file directly.
