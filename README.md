# AI-Powered Visualizations for Spaceborne Biological Experiments

## Project Overview
Spaceborne biological experiments offer valuable insights into how biological systems respond to the unique environment of space. However, the complexity involved in these experiments—ranging from their execution in space to specialized hardware and return to Earth—poses a significant challenge for many scientists. 

This project addresses that challenge by providing an **AI-powered tool** that automates the generation of **graphical abstracts** and **interactive visualizations**. The tool leverages **Generative AI** to help scientists with minimal knowledge of space biology quickly understand and explore complex experiment data from **NASA’s Open Science Data Repository (OSDR)**. This tool is scalable, initially designed for datasets from the **Rodent Research Missions OSD-379 and OSD-665**, but can be expanded to include other spaceborne experiments.

## Key Features
- **Automated Graphical Abstracts**: Automatically generates visual summaries of biological experiments, outlining subjects, treatments, timelines, and key findings.
- **Interactive Visualizations**: Users can explore different experiment parameters, treatments, and results through an intuitive dashboard.
- **Scalability**: While the tool currently supports two ISS datasets, it can easily scale to handle more data from NASA's OSDR.
- **Accessibility**: Designed for scientists and researchers with little experience in space experiments to understand data quickly and efficiently.
- **Contextual Insights**: The tool provides contextual connections between similar experiments and datasets within NASA's repository, enhancing understanding and discovery.

## How It Works
1. **Data Ingestion**: The tool imports structured metadata and data from NASA’s **Open Science Data Repository (OSDR)**. For now, it focuses on two key datasets:
    - **Rodent Research-1 (OSD-379)**: Investigating the biological effects of space on rodent subjects.
    - **Rodent Research-23 (OSD-665)**: A follow-up study focusing on long-term biological adaptations in space.
   
2. **AI-Driven Visualization**: Using **Generative AI**, the tool generates graphical abstracts summarizing the experimental structure, including:
   - Number of subjects per group.
   - Treatments applied to each group.
   - Key events, such as launch to the ISS and return to Earth.
   - Major outcomes of the study.

3. **Interactive Dashboard**: The tool offers a **user-friendly interface** where scientists can:
   - Explore individual experiments.
   - Compare experiment parameters, such as subjects, treatments, and outcomes.
   - Filter data based on various criteria, such as experiment timeline or treatments used.

4. **Contextualization**: By making connections to other related experiments in the OSDR, the tool provides additional insights that may support ongoing research or spark new discoveries.

## Data Sources
The project utilizes two key datasets from NASA’s Open Science Data Repository:
- **Rodent Research-1 (OSD-379)**: [Explore dataset](https://osdr.nasa.gov)
- **Rodent Research-23 (OSD-665)**: [Explore dataset](https://osdr.nasa.gov)

These datasets include structured metadata, experiment conditions, treatments, and results, all of which are fed into the AI model to generate meaningful visualizations.

## Installation and Setup
To set up and run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/space-experiment-visualizations.git
