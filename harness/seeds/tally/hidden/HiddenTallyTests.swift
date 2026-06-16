import XCTest
@testable import Tally

// HIDDEN grader -- copied into Tests/TallyTests/ only AFTER the agent finishes.
// The large workload makes any non-serialized (raced) implementation lose
// updates and fail deterministically, so an `actor`-style fix is required.
final class HiddenTallyTests: XCTestCase {
    func testTotalLarge() async {
        let r = await total(workers: 64, perWorker: 5000)
        XCTAssertEqual(r, 320000)
    }

    func testTotalZeroWorkers() async {
        let r = await total(workers: 0, perWorker: 100)
        XCTAssertEqual(r, 0)
    }

    func testTotalManyWorkers() async {
        let r = await total(workers: 200, perWorker: 1000)
        XCTAssertEqual(r, 200000)
    }
}
