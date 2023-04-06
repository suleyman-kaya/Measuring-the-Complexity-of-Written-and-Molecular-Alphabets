# Project: _**Measuring the Complexity of Written and Molecular Alphabets**_

You can access the documentation of the tool that will allow you to learn the fractal dimension of images produced by Pymol from [here.](tools/usage.md)

## Project description

Various human languages transmit information by encoding it in written alphabets (for example, the one being used here). The symbols (letters, but also numerals in math) in these alphabets must be able to represent all of the vocal phonemes or conceptual units which the language needs to be intelligible, and are generally arbitrary, though sometimes they descend from earlier pictographs. These symbols need to be distinguishable among themselves, which implies they have significant and easily discernible structural differences (e.g., "0" vs. "1", "v" vs. "w"). The complexity and differences among these symbols can be quantified by various metrics, as can the processes needed to construct them (such as the number of writing strokes or stroke order). Similarly, biology uses molecular alphabets, most notably the nucleobases and amino acids, which are used to construct biopolymers (polynucleotides and proteins). In contrast with written language, these symbols are three dimensional and have specific functional properties, so the metrics which make these symbols unique may be different, or there may be deep structural similarities in the ways systems select symbolic alphabets. This project aims to develop complexity metrics for both human linguistic and biological molecular alphabets, compare their distributions, and understand how information is compressed into structure and selected for functional use in alphabets.

## What's happening?

This project focuses on measuring the complexity of written and molecular alphabets. Written alphabets are used by human languages to encode and communicate information, and these symbols must be able to represent all the sounds and concepts needed for the language to be understood. These symbols are generally arbitrary but have easily discernible structural differences that distinguish them from one another, such as "0" vs. "1" or "v" vs. "w". Complexity metrics, such as stroke order or the number of writing strokes, can be used to quantify these differences.

Similarly, biology uses molecular alphabets, such as nucleobases and amino acids, which are used to construct biopolymers. These symbols are three-dimensional and possess unique functional properties, making the metrics used to measure their complexity different from those used for written language. The aim of this project is to develop complexity metrics for both written and molecular alphabets, compare their distributions, and gain insight into how information is structured and selected for functional use in alphabets.

## What do you mean by "Molecular Alphabets"?

A molecular alphabet is a set of basic units that encode and represent information in biological molecules. In the case of DNA and RNA, the molecular alphabet is composed of four nucleotide bases, namely adenine (A), guanine (G), cytosine (C), and thymine (T) in DNA, or uracil (U) in RNA. These bases form the genetic code that carries the instructions necessary for the synthesis of proteins. Proteins, in turn, are constructed using a different molecular alphabet that consists of 20 amino acids.

These molecular alphabets are fundamental to the biological processes that govern life. They allow cells to replicate and produce the proteins necessary for their survival and function.

## What is molecular complexity?

Molecular complexity refers to the level of intricacy or diversity in the chemical structures and properties of molecules. This means that some molecules can be simple, with only a few unique features, while others can be very complex, with many different features.

In the field of biology, molecules such as DNA, RNA, and proteins are highly complex and have unique functional properties that allow them to carry out specific biological functions. Understanding the complexity of these molecules is important for understanding how they work and for developing new drugs and therapies that target specific molecules or molecular systems.

Overall, molecular complexity is a measure of the diversity and intricacy of the chemical structures and properties of molecules, and it plays an important role in many fields of science, including biology, chemistry, and pharmacology.

## Molecular complexity calculation methods?

There are several types of molecular complexity calculation methods, including graph-based, information theory-based, topological indices, and fragment-based methods. Graph-based methods use the molecular graph to calculate different complexity indices, while information theory-based methods use concepts from information theory to quantify complexity. Topological indices are numerical descriptors that reflect different aspects of molecular structure, and fragment-based methods divide a molecule into smaller parts to calculate complexity indices based on their properties.

There are various information theory-based methods that can be used to calculate molecular complexity. Some of these methods are:

1.  **Atom Count Method**: Molecular complexity depends on the number of atoms in the molecule. This method estimates molecular complexity by calculating the number of atoms in a molecule.
    
2.  **Topological Index Method**: This method is based on a mathematical formula that depends on the number and length of bonds in the molecular structure. Topological indices are numerical parameters used to describe the structure of a molecule.
    
3.  **Quantum Chemistry Methods**: Quantum chemistry is a set of mathematical and physical methods used to calculate the structural and reactive properties of molecules. These methods include density functional theory, Hartree-Fock method, and ab initio methods.
    
4.  **Artificial Intelligence Methods**: In recent years, artificial intelligence techniques have also been used to predict molecular complexity. Specifically, deep learning techniques are used to predict the structure and properties of molecules.

## Calculating molecular complexity by fractal dimension

The process of calculating molecular complexity with fractal dimension is as follows:

1.  The 3D structure of the molecule is created using a molecular drawing program.
    
2.  The drawing of the molecule is processed using a fractal analysis software that calculates the fractal dimension to identify the scale-independent properties of the molecule.
    
3.  The calculation of fractal dimension is performed by analyzing the molecule's different properties at different scales, including the surface area, volume, branching ratio, and other factors.
    
4.  The results of the fractal dimension calculation are used to evaluate molecular complexity. The higher the fractal dimension of the molecule, the higher its molecular complexity.

Ayrıntılı bilgi için: [1] ["Molecular Complexity Calculated by Fractal Dimension", 30 January 2019, Modest von Korff, Thomas Sander](https://www.nature.com/articles/s41598-018-37253-8) ***

### 3D structure creation of the Molecule

Here are some popular molecular drawing programs:

1.  ChemDraw: A commonly used program for drawing and editing chemical structures. It is available for both Windows and Mac operating systems.
    
2.  MarvinSketch: A free program used to draw, edit, and analyze chemical structures. It is available for Windows, Mac, and Linux operating systems.
    
3.  Avogadro: A free and open-source molecular modeling program. It is available for both Windows and Mac operating systems.
    
4.  PyMOL: A program used to visualize the 3D structures of proteins and other large biomolecules. It is available for Windows, Mac, and Linux operating systems.
    
5.  VMD: A program used to visualize the 3D structures of biomolecules. It is available for Windows, Mac, and Linux operating systems.

Choosing among these programs depends on the type of molecule and the user's preferences. For example, PyMOL or VMD may be more suitable for analyzing the structure of a protein, while ChemDraw or MarvinSketch may be more suitable for drawing the structure of small organic molecules.

### "Box-Counting" approach for calculating fractal dimension

The box-counting approach is a popular method for calculating the fractal dimension of an object, including molecules. This method involves dividing the object into a series of boxes of decreasing size, and then counting the number of boxes that contain at least one point or atom from the molecule. The fractal dimension is then obtained by fitting a straight line to a plot of the logarithm of the number of boxes versus the logarithm of the box size.

The box-counting approach works as follows:

1.  Divide the molecule into a grid of equally-sized boxes.
2.  Count the number of boxes that contain at least one atom from the molecule.
3.  Reduce the size of the boxes and repeat step 2 until the boxes become very small or the entire molecule is covered.
4.  Plot the logarithm of the number of boxes versus the logarithm of the box size.
5.  Determine the slope of the line that fits the data points on the plot.
6.  The slope of the line is the fractal dimension of the molecule.

The box-counting method is based on the idea that the fractal dimension of an object is related to the scaling behavior of the object as its size is changed. When the object is magnified, the number of boxes needed to cover the object increases, and the fractal dimension can be calculated by measuring the rate at which the number of boxes increases with decreasing box size.

In practice, the box-counting approach can be implemented using computer algorithms that generate grids of boxes and count the number of boxes containing atoms from the molecule. The resulting data can then be plotted and analyzed to calculate the fractal dimension of the molecule.

# Here are a few resources
[2] ["From Molecules to Life: Quantifying the Complexity of Chemical and Biological Systems in the Universe", 2017 Dec 19, Thomas Böttcher](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5794832/pdf/239_2017_Article_9824.pdf)

[3] ["Measuring the Complexity of Writing Systems", January 1994, Journal of Quantitative Linguistics, Antal Van den Bosch from Koninklijke Nederlandse Akademie van Wetenschappen, Alain Content from Université Libre de Bruxelles, Walter Daelemans from University of Antwerp, Beatrice de Gelder from Maastricht University](https://www.researchgate.net/publication/220469275_Measuring_the_Complexity_of_Writing_Systems)

[4] ["Molecular complexity: a simplified formula adapted to individual atoms", 1987-27-2, James B. Hendrickson, Ping Huang, and A. Glenn Toczko](https://pubs.acs.org/doi/pdf/10.1021/ci00054a004)

[5] [Fractal Dimension of 2D Images](https://github.com/brian-xu/FractalDimension)

[6] [A robust algorithm for the fractal dimension of images and its applications to the classification of natural images and ultrasonic liver images](https://www.sciencedirect.com/science/article/abs/pii/S0165168409005210?via%3Dihub)
