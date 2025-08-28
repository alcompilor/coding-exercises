using BookingsApi;

var builder = WebApplication.CreateBuilder(args);

// Dependency Injection for Controllers/Services
DependencyInjection.ConfigureControllers(builder.Services);
DependencyInjection.ConfigureServices(builder.Services);

var app = builder.Build();

// Map controller endpoints
app.MapControllers();

app.Run();
