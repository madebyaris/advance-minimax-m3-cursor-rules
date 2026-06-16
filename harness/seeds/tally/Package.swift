// swift-tools-version:6.0
import PackageDescription

let package = Package(
    name: "Tally",
    platforms: [.macOS(.v13)],
    targets: [
        .target(name: "Tally"),
        .testTarget(name: "TallyTests", dependencies: ["Tally"]),
    ]
)
