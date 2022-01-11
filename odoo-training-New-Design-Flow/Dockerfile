FROM odoo:14.0
LABEL maintainer="Bloopark Systems. <info@bloopark.de>"

USER root
# Mount Customize /odoo/"addons" folders for users addons
RUN mkdir -p /mnt/extra-addons

COPY ./requirements.txt /odoo/requirements_c.txt
# Install Chromium
RUN apt-get update && pip3 install --upgrade pip \
    && pip3 install -r /odoo/requirements_c.txt

# RUN chown -R odoo:odoo /odoo/enterprise
# Set default user when running the container
USER odoo
