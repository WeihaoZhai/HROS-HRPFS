# Changelog

This document records all important changes to the Habitat Radiomics project.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-19

### Added Features
- Voxel-level radiomics feature extraction functionality
- Automatic clustering analysis based on K-means
- Optimal cluster number selection using Calinski-Harabasz score
- Habitat mask generation and visualization
- Progress tracking and checkpoint/resume functionality
- Rich visualization features (feature distributions, clustering results, 3D mask slices)
- Complete project documentation and API reference
- Jupyter Notebook usage examples

### Core Features
- **Feature Extraction**: Multiple radiomics features based on PyRadiomics
- **Data Processing**: Automatic feature combination and preprocessing
- **Clustering Analysis**: PCA dimensionality reduction + K-means clustering
- **Mask Generation**: Multi-cluster habitat mask output
- **Visualization**: matplotlib/seaborn visualization components

### Technical Features
- Support for multiple medical image formats (NIFTI, NRRD, etc.)
- Memory optimization and large dataset processing
- Error handling and logging
- Modular design for easy extension

### Documentation
- Detailed README documentation
- Complete API documentation
- Usage examples and tutorials
- Configuration file instructions

---

## Future Version Plans

### [1.1.0] - Planned
- [ ] Multi-threaded parallel processing support
- [ ] More clustering algorithm options
- [ ] Interactive visualization interface
- [ ] Configuration file validation tools

### [1.2.0] - Planned  
- [ ] Deep learning feature extraction support
- [ ] Statistical analysis and survival analysis functionality
- [ ] Web interface development
- [ ] Docker containerized deployment

---

## Contributing Guidelines

Welcome to submit Issues and Pull Requests to improve the project!

Please ensure:
1. Follow existing code style
2. Add appropriate test cases
3. Update relevant documentation
4. Record important changes in this file 