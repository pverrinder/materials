## Plans for My Code

I want to eventually include the following (roughly in order of importance).


- Optical dispersion, eps(eV or freq.) 
- Material constants (function of composition for ternary and quaternary)
    - Bandgap
    - Lattice constant
    - Effective mass
    - etc. etc.
- QW calculations
    - Strain and critical thickness
    - Energy levels
- Doping dependence
    - Bandgap, epsilon, effective masses
- Temperature dependence of material parameters, especially:
    - epsilon, bandgap, lattice constant, effective mass

```
class IIIV binary:
    name 
    
    Common constants:
    - lattice
    - bandgap
    - effective mass

    Dispersion relations:
    - get_nk() to read tabulated nk-data (e.g. from refracitveindex.info
    - parameters for calculating epsilon(eV), as applicable
        - e.g. Adachi 1989, Aspnes?, Others...
    - calculate_epsilon()
        - some materials may have multiple options for calculating eps
        according to different literature models.

    Temperature Dependence:
    - Calculate material properties at specific temperature

    Free Carrier/Doping Effects:
    - Dispersion and other properties as a function of free carriers or
    doping concentration
```

