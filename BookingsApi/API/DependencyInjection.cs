using BookingsApi.Repositories;
using BookingsApi.Services;
using BookingsApi.Interfaces;

namespace BookingsApi
{
    public static class DependencyInjection
    {
        public static void ConfigureServices(IServiceCollection services)
        {
            services.AddScoped<IBookingService, BookingService>();
            services.AddScoped<IBookingRepository, BookingRepository>();
        }

        public static void ConfigureControllers(IServiceCollection services)
        {
            services.AddControllers();
        }
    }
}