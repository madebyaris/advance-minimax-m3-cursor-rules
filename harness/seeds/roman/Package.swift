// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "RomanKit",
    targets: [
        .target(name: "RomanKit"),
        .testTarget(name: "RomanKitTests", dependencies: ["RomanKit"]),
    ]
)
