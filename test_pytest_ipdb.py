def test_test():
    """ipdb.set_trace() should drop us into an ipdb debugger

    (not break with
        AttributeError: DontReadFromInput instance has no attribute 'encoding'
    )
    """

    # press 'c' to complete test
    import ipdb; ipdb.set_trace()
