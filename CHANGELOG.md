# Changelog

<!---
Template

## [x.x.x] - 20xx-xx-xx

### Added

- this
- that

### Changed

- this
- that

### Removed

- this
- that

--->

## [Unreleased]

### Added

- [[Boat]] Add setter methods for rudderAngle
- [[GUI]] Display Sailor Waypoints on [mapView]
- [[GUI]] Add goto start and goto end button
- [[GUI]] Hide and show parts of [mapView] and [boatInspector] from the menu point "View"
- [[GUI]] Add [valueInspector] to view raw values

### Changed

- [[GUI]] Display mainSailAngle and rudderAngle in [boatInspector]
- [[Sailor]] Use index instead of deleting [Commands] after executing them

## [0.0.1] - 2021-04-13

### Added

- [[Simulation]] Basic simulation features
- [[World]] Basic functions for World
- [[Boat]] Basic boat behavior
- [[Sailor]] can reach waypoints into all directions
- [[Wind]] Basic wind system
- [[GUI]] Basic GUI for displaying a simulation



<!--- Versions --->
[Unreleased]: https://github.com/mfbehrens99/sailsim/compare/v0.0.1...HEAD
[0.0.2]: https://github.com/mfbehrens99/sailsim/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/mfbehrens99/sailsim/releases/tag/v0.0.1

<!--- Parts --->
[Simulation]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/simulation/Simulation.py
[World]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/world/World.py
[Boat]:https://github.com/mfbehrens99/sailsim/blob/main/sailsim/boat/Boat.py
[Sailor]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/sailor/Sailor.py
[Commands]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/sailor/Commands.py
[Wind]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/wind/Wind.py
[GUI]: https://github.com/mfbehrens99/sailsim/tree/main/sailsim/gui
[mapView]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/gui/mapView.py
[boatInspector]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/gui/boatInspector.py
[valueInspector]: https://github.com/mfbehrens99/sailsim/blob/main/sailsim/gui/valueInspector.py
[utils]: https://github.com/mfbehrens99/sailsim/tree/main/sailsim/utils
