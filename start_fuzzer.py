import fuzzing_worker as worker

if __name__ == "__main__":

    worker.RunFuzzer.apply_async(["E2396553-B35E-4CFF-8E0C-207ABF09C63A", "TestJpgRun", "pits/foo/jpg.pit"])
    worker.RunFuzzer.apply_async(["C280168B-B24C-4FA4-8508-7AF18089D1F0", "TestGifRun", "pits/foo/gif.pit"])
