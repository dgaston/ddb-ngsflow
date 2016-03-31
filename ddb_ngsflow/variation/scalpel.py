"""
.. module:: scalpel
   :platform: Unix, OSX
   :synopsis: A wrapper module for calling scalpel.

.. moduleauthor:: Daniel Gaston <daniel.gaston@dal.ca>


"""

import os

from ddb_ngsflow import pipeline


def scalpel_single(job, config, sample, samples, input_bam):
    """Run Scalpel on an an unmatched tumour sample and call somatic variants
    :param config: The configuration dictionary.
    :type config: dict.
    :param sample: sample name.
    :type sample: str.
    :param input_bam: The input_bam file name to process.
    :type input_bam: str.
    :returns:  str -- The output vcf file name.
    """

    cwd = os.getcwd()
    output_dir = os.path.join(cwd, "{}-scalpel-output".format(sample))
    scalpel_vcf = os.path.join(output_dir, "variants.indel.vcf")
    fixed_vcf = "{}.scalpel.vcf".format(sample)
    logfile = "{}.scalpel.log".format(sample)
    logfile2 = "{}.scalpel_fix.log".format(sample)

    scalpel_command = ("{}".format(config['scalpel']['bin']),
                       "--single",
                       "--intarget",
                       # "--covthr",
                       # "3",
                       # "--lowcov",
                       # "1",
                       "--ref",
                       "{}".format(config['reference']),
                       "--bed",
                       "{}".format(samples[sample]['regions']),
                       "--format",
                       "vcf",
                       "--numprocs",
                       "{}".format(config['scalpel']['num_cores']),
                       "--bam",
                       "{}".format(input_bam),
                       "--dir",
                       "{}".format(output_dir))

    fix_sample_name_command = ("cat",
                               "{}".format(scalpel_vcf),
                               "|",
                               "sed",
                               "'s/sample/{}/g'".format(sample),
                               ">",
                               "{}".format(fixed_vcf))

    job.fileStore.logToMaster("Scalpel Command: {}\n".format(scalpel_command))
    pipeline.run_and_log_command(" ".join(scalpel_command), logfile)

    job.fileStore.logToMaster("Scalpel Fix Command: {}\n".format(fix_sample_name_command))
    pipeline.run_and_log_command(" ".join(fix_sample_name_command), logfile2)

    return scalpel_vcf
