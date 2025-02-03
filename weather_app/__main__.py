import click

from .utils import format_weather_data, get_weather


@click.command()
@click.option('--lat', type=float)
@click.option('--long', type=float)
def main(lat, long):
    weather_data = get_weather(lat, long)
    print(format_weather_data(weather_data))


if __name__ == '__main__':
    main()
