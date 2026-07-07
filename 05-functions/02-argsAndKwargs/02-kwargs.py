# Kwargs

# Kwargs or key word arguements are pass in as a dictionary
# this is due to 3 reasons:
# 1. The order of the arguments doesn't matter
# 2. You can pass in any number of args
# 3. The names of the arguments don't have to be unique

def program_version(version: str, **kwargs) -> None:
    print('version', version)
    print('System:', kwargs)

    if 'bitrate' in kwargs.keys():
        print(f"bitrate set to : {kwargs.get("bitrate")}")


program_version('1.5', bitrate=1.8, system='Windows')

# The kwargs are 2 asterisks and the name of the variable is kwargs
# They are bitrate and system in this program.
# You will need additional code to interact with them.
# like kwargs.get()
