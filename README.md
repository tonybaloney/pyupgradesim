# pyUpgradeSim

A tool for automating load tests against a list of Python versions using locust, Docker and DjangoQ schedulers.

## Requirements

- Docker
- Python 3.8+
- The Python packages in `requirements.txt`, use `pip install -r requirements.txt` to install them

## Usage

Run `make images` to build the container images

Run `make web` to run the web application, launches on port 8000 by default

## Related Paper

Please see the [WWW '23 Companion](https://dl.acm.org/doi/10.1145/3543873.3587338) for the associated paper for this tool.

A bibtex entry is available below to reference this paper.

```bibtex
@inproceedings{10.1145/3543873.3587338,
  author = {Shaw, Anthony and Beheshti, Amin},
  title = {Measuring Potential Performance Gains of Python Web Applications with PyUpgradeSim},
  year = {2023},
  isbn = {9781450394192},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3543873.3587338},
  doi = {10.1145/3543873.3587338},
  abstract = {Python is a popular programming language for web development. However, optimizing the performance of Python web applications is a challenging task for developers. This paper presents a new approach to measuring the potential performance gains of upgraded Python web applications. Our approach is based on the provision of an interactive service that assists developers in optimizing their Python code through changes to the underlying system. The service uses profiling and visualization techniques to identify performance bottlenecks. We demonstrate and evaluate the effectiveness of our approach through a series of experiments on real-world Python web applications, measuring performance differences in between versions and the benefits of migrating at a reduced cost. The results show promising improvement in performance without any required code changes.},
  booktitle = {Companion Proceedings of the ACM Web Conference 2023},
  pages = {164–167},
  numpages = {4},
  keywords = {Performance, Web Frameworks, Benchmarks, Estimation, Python},
  location = {Austin, TX, USA},
  series = {WWW '23 Companion}
}
```
