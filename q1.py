def get_contents(fname):
    try:
        with open(fname, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

