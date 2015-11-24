__author__ = 'dgaston'

__author__ = 'dgaston'

# Standard packages
import sys
import argparse
import multiprocessing

# Third-party packages
from toil.job import Job

# Package methods
from ngsflow import annotation
from ngsflow import read_sample_sheet
from ngsflow.utils import configuration
from ngsflow.utils import utilities
from ngsflow.variation import variation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--samples_file', help="Input configuration file for samples")
    parser.add_argument('-c', '--configuration', help="Configuration file for various settings")
    Job.Runner.addToilOptions(parser)
    args = parser.parse_args()
    # args.logLevel = "INFO"

    sys.stdout.write("Parsing configuration data\n")
    config = configuration.configure_runtime(args.configuration)

    sys.stdout.write("Parsing sample data\n")
    samples = configuration.configure_samples(args.samples_file)

    num_cores = multiprocessing.cpu_count()

    root_job = Job.wrapJobFn(utilities.spawn_batch_jobs)

    for sample in samples:
        on_target_job = Job.wrapJobFn(utilities.bcftools_filter_variants_regions, config, sample,
                                      samples[sample]['vcf'], cores=num_cores, memory="1G")
