from main import get_positions
try:
    print(get_positions())
except Exception as e:
    import traceback
    traceback.print_exc()
