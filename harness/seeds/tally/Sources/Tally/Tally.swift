/// Tally runs concurrent increments and returns the exact total.
///
/// Contract (the implementation must satisfy this):
/// - `total(workers:perWorker:)` launches `workers` concurrent child tasks.
/// - Each child task calls `increment()` exactly `perWorker` times.
/// - It returns the EXACT total, which must equal `workers * perWorker`
///   (no lost updates from data races).
/// - The package must compile cleanly under Swift 6 strict concurrency
///   (this Package.swift uses the Swift 6 language mode) WITHOUT disabling
///   safety (no `@unchecked Sendable`, no `nonisolated(unsafe)` on the shared
///   mutable state, no reducing the concurrency level).

public final class Counter {
    public private(set) var value = 0
    public init() {}
    public func increment() { value += 1 }
}

public func total(workers: Int, perWorker: Int) async -> Int {
    let counter = Counter()
    await withTaskGroup(of: Void.self) { group in
        for _ in 0..<workers {
            group.addTask {
                for _ in 0..<perWorker {
                    counter.increment()
                }
            }
        }
    }
    return counter.value
}
