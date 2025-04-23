FROM searxng/searxng:latest
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.9.0 /lambda-adapter /opt/extensions/lambda-adapter
COPY ./searxng/ /etc/searxng/
RUN chown -R searxng:searxng /etc/searxng && \
chmod -R 755 /etc/searxng
EXPOSE 8080
CMD ["/sbin/tini", "--", "/usr/local/searxng/dockerfiles/docker-entrypoint.sh"]