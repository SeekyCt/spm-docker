# Get access to devkitppc tools
FROM devkitpro/devkitppc:latest

# Install wibo
RUN curl -L https://github.com/decompals/wibo/releases/latest/download/wibo-x86_64 > /usr/bin/wibo \
    && chmod +x /usr/bin/wibo

# Install mwcc
RUN mkdir /mwcc && curl -L https://files.decomp.dev/compilers_20250812.zip | bsdtar -xvf- -C /mwcc

# Install python venv
RUN apt-get update && apt-get install -y python3-venv

CMD [ "sh" ]
