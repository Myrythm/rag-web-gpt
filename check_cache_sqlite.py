try:
    from langchain_community.cache import SQLiteCache
    print("Found in langchain_community")
except ImportError:
    try:
        from langchain.cache import SQLiteCache
        print("Found in langchain")
    except ImportError:
        print("Not found")
