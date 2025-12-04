try:
    from langchain.cache import InMemoryCache
    print("Found InMemoryCache in langchain.cache")
except ImportError:
    try:
        from langchain_core.caches import InMemoryCache
        print("Found InMemoryCache in langchain_core.caches")
    except ImportError:
        print("Not found")
