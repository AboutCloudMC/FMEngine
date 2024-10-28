# FMEngine [Work in Progress]

FMEngine is a modular and basic Python engine designed to perform various physics, math, and graphical computations.
This engine is currently only usable to simulate the effects of mass, force, velocity and momentum on objects
and how they effect each other.
Note: The **GraphicsComponent** uses pygame to visualise the simulation.

## Project Structure

- **FMEngine.py** - Main engine file to initialize and manage components.
- **GraphicsComponent.py** - Handles graphical rendering and visualization tasks.
- **MathComponent.py** - Provides mathematical functions and calculations.
- **PhysicsComponent.py** - Manages physics-related computations and simulations.
- **testsim.py** - Contains a test simulation to test the funtionality.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/FMEngine.git
   cd FMEngine
   ```

2. **Write your own simulation using the FMEngine**:
   ```python
   import FMEngine as fm
   ```
   
3. **Run your simulation**:
   ```bash
   python yoursim.py
   ```

## License

This project is open source and available under the [MIT License](LICENSE).
