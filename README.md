# Habitat Radiomics

A Python toolkit for medical image radiomics analysis, focusing on voxel-level feature extraction, clustering analysis, and habitat mask generation.

## Features

- **Voxel-level Feature Extraction**: PyRadiomics-based voxel-level radiomics feature extraction
- **Automatic Clustering Analysis**: K-means clustering with Calinski-Harabasz score optimization for optimal cluster number
- **Habitat Mask Generation**: Generate habitat masks for different clusters for further analysis
- **Progress Tracking**: Support for checkpoint and resume functionality to avoid redundant computations
- **Visualization**: Rich visualization capabilities including feature distributions, clustering results, and 3D mask slices

## Project Structure

```
habitat-radiomics/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore configuration
├── src/                              # Source code directory
│   ├── __init__.py                   # Python package initialization
│   ├── main.py                       # Main program entry point
│   ├── feature_extraction.py         # Feature extraction module
│   ├── progress_tracker.py           # Progress tracking module
│   └── visualization.py              # Visualization module
├── config/                           # Configuration files
│   └── exampleVoxel.yaml            # Radiomics feature extraction configuration example
├── examples/                         # Examples and tutorials
│   ├── basic_usage.py                # Basic usage example
│   └── notebooks/                    # Jupyter Notebook examples
│       ├── Habitat_Radiomics_main.ipynb     # Main analysis workflow
│       └── Process_New_Data.ipynb           # New data processing workflow
├── docs/                             # Documentation directory
│   └── API.md                        # API documentation
└── tests/                            # Test directory
    └── __init__.py
```

## Installation

### Requirements

- Python 3.7+
- Recommended: Anaconda/Miniconda

### Installation Steps

1. Clone the repository
```bash
git clone <your-repository-url>
cd habitat-radiomics
```

2. Create virtual environment (recommended)
```bash
conda create -n habitat-radiomics python=3.8
conda activate habitat-radiomics
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from src.main import main

# Set parameters
params = {
    'imgfolder': '/path/to/images',
    'maskfolder': '/path/to/masks', 
    'yaml': './config/exampleVoxel.yaml',
    'min_clusters': 2,
    'max_clusters': 10
}

# Run analysis
features_df, labels, optimal_k = main(**params)
```

### Configuration

Configure radiomics feature extraction parameters in `config/exampleVoxel.yaml`:

```yaml
imageType:
  Original: {}

featureClass:
  firstorder:
    - Entropy
  ngtdm:

setting:
  binWidth: 25
  label: 1
  additionalInfo: False

voxelSetting:
  kernelRadius: 4
  maskedKernel: true
  initValue: nan
```

## Output Results

After analysis completion, the following will be generated in the `./results` directory:

- `features/`: Feature files
  - `voxel_features/`: Voxel-level features (organized by feature type)
  - `combined_features.pkl`: Combined feature data
- `plots/`: Visualization results
  - `feature_distributions.png`: Feature distribution plots
  - `clustering_results.png`: Clustering result plots
  - `calinski_harabasz_scores.png`: Clustering score plots
  - `habitat_*.png`: Habitat mask visualizations
- `habitats/`: Habitat mask files
  - `habitat_*.nrrd`: Main habitat masks
  - `habitat_*_cluster_*.nrrd`: Individual cluster habitat masks

## Progress Tracking

The program supports checkpoint and resume functionality:
- Automatically saves progress for each step
- Skips completed steps when rerunning
- Progress information saved in `./results/progress.json`

## Examples and Tutorials

### Jupyter Notebooks

Detailed usage examples are provided in the `examples/notebooks/` directory:

1. `Habitat_Radiomics_main.ipynb`: Complete analysis workflow demonstration
2. `Process_New_Data.ipynb`: New data processing workflow

### Python Script Examples

See `examples/basic_usage.py` for basic usage methods.

## API Documentation

For detailed API documentation, please refer to `docs/API.md`.

## Dependencies

Main dependencies include:
- pyradiomics: Radiomics feature extraction
- SimpleITK: Medical image processing
- scikit-learn: Machine learning and clustering
- matplotlib, seaborn: Data visualization
- pandas, numpy: Data processing

## Important Notes

1. Ensure input images and masks are in compatible formats (e.g., NIFTI, NRRD)
2. Image and mask filenames should correspond and match
3. Large dataset processing may take considerable time; progress tracking is recommended
4. Memory usage depends on image size and number of features

## Contributing

Bug reports, feature requests, and code contributions are welcome. Please ensure:
1. Code follows PEP 8 standards
2. Appropriate comments and documentation are added
3. Necessary test cases are included

## License

[Add your license information here]

## Citation

If you use this tool in your research, please consider citing:

```
[Your paper citation information]
```

## Contact

For questions or suggestions, please contact:
- Email: [Your email]
- GitHub Issues: [Project Issue page] 