import glob

SAMPLES, = glob_wildcards(f"{config['base_file_paths']['spectra']}/{{sample}}.{config['spectra_extension']}")

print(SAMPLES)

rule all:
    input:
        report = f"{config['base_file_paths']['results']}/diann-output/diann-output.tsv"


rule diann_convert_library:
    input:
        library = config['libraries']['spectral_library']
    output:
        library = f"{config['libraries']['spectral_library']}.speclib"
    params:
        diann = config['diann']['exe']
    shell:
        (
            "{params.diann} "
            "--lib {input.library}"
        )

rule diann_create_file_list:
    input:
        input_files = expand(f"{config['base_file_paths']['spectra']}/{{sample}}.{config['spectra_extension']}", sample=SAMPLES)
    output:
        file_list = f"{config['base_file_paths']['results']}/file_list.txt"
    run:
        with open(output.file_list, 'w') as outfile:
            for input_file in input.input_files:
                print(input_file)
                file_line = f"--f {input_file}\n"
                outfile.write(file_line)


rule diann_extract_signal:
    input:
        library = f"{config['libraries']['spectral_library']}.speclib",
        file_list = f"{config['base_file_paths']['results']}/file_list.txt"
    output:
        output_file = f"{config['base_file_paths']['results']}/diann-output/diann-output.tsv"
    params:
        q_value = 0.01,
        verbose = 1,
        diann = config['diann']['exe'],
    threads:
        config['diann']['threads']
    shell:
        (
            "{params.diann} "
            "--lib {input.library} "
            "--qvalue {params.q_value} "
            "--no-prot-inf "
            "--threads {threads} "
            "--reanalyse "
            "--report-lib-info "
            "--mass-acc 15 "
            "--mass-acc-ms1 15 "
            "--regular-swath "
            "--smart-profiling "
            "--direct-quant "
            "--verbose {params.verbose} "
            "--out {output.output_file} "
            "--cfg {input.file_list}--"
        )
