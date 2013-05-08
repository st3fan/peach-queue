
import fuzzing_worker

fuzzing_worker.RunFuzzer.apply_async(["E2396553-B35E-4CFF-8E0C-207ABF09C63A", "TestJpgRun", "pits/foo/jpg.pit"], queue="fuzzer")

